import csv
import requests

from django.db import models

class Line(models.Model):
    secret = models.CharField(max_length=16)
    name = models.CharField(max_length=12)

    def __str__(self):
        return self.name

    def get_url(self, fmt=None):
        if fmt is None:
            fmt = "csv"
        url = "https://control.aa.net.uk/cqmdirect.cgi/{}/{}.{}".format(self.secret, self.name, fmt)
        return url

    def request_fmt(self, fmt=None):
        if fmt is None:
            fmt = "csv"
        response = requests.get( self.get_url(fmt) )
        return response

    def read_csv(self, r=None):
        if r is None:
            r = self.request_fmt(fmt="csv")
        c = csv.DictReader( r.text.splitlines() )
        return c

    def csv_convert(self, c=None):
        if c is None:
            c = self.read_csv()

        convert = {
            # Convert the headers from the CSV into model-friendly names
            # for expansion (see self.bandwidth() )
            "Time": "time",
            "Period": "period",
            "Polls Sent": "sent",
            "%Fail": "fail",
            "Latency Min": "latency_min",
            "Av": "latency_av",
            "Max": "latency_max",
            "Traffic (bit/s) Rx": "traffic_rx",
            "Tx": "traffic_tx",
            "Score": "score",
        }

        bwe = []
        bw = {
            # Add pointer to this Line
            "line": self
        }

        for entry in c:
            for key in entry.keys():
                bw[ convert[key] ] = entry[key]
            bwe.append( bw )

        return bwe

    def bandwidth(self, bwe=None):
        if bwe is None:
            bwe = self.csv_convert()

        ret = []
        for entry in bwe:
            # unpack dict keys as model fields
            # see self.csv_convert()
            bw = Bandwidth( **entry )
            ret.append( bw.save() )

        return ret

class Bandwidth(models.Model):
    # Bandwidth record for provided line
    line = models.ForeignKey(Line)

    # Fields from AAISP
    # see Line.csv_convert()
    time = models.DateTimeField()
    period = models.IntegerField()
    sent = models.IntegerField()
    fail = models.IntegerField()
    latency_min = models.IntegerField()
    latency_av = models.IntegerField()
    latency_max = models.IntegerField()
    traffic_rx = models.IntegerField()
    traffic_tx = models.IntegerField()
    score = models.IntegerField()
