import csv

from django.test import TestCase
from django.db.utils import IntegrityError

from .models import Bandwidth, Line

class BandwidthTestCases(TestCase):
    def setUp(self):
        self.line = Line(secret="", name="")
        self.line.save()

    def test_duplicate_times(self):
        """
        The data source contains data for the last 24 hours, so this will be run more often than that.
        Prove that the same data will not be inserted into the database again
        """
        dummy = {
            "line": self.line,
            "time": "2017-09-13 07:11:00",
        }

        # Populate the Bandwith model with dummy data
        for key in 'period sent fail latency_min latency_av latency_max traffic_rx traffic_tx score'.split(" "):
            dummy[ key ] = 0

        Bandwidth(**dummy).save()

        with self.assertRaises(IntegrityError):
            Bandwidth(**dummy).save()

    def test_csv_import(self):
        """
        With a copy of real data, test that the model can save data
        """

        c = csv.DictReader("""Time,Period,Polls Sent,%Fail,Latency Min,Av,Max,Traffic (bit/s) Rx,Tx,Score
2017-09-12 08:00:00,100,100,0,6376000,6807000,7345000,19670,278400,1
2017-09-12 08:01:40,100,100,0,6412000,6899000,9343000,19190,294300,1
2017-09-12 08:03:20,100,100,0,6361000,6873000,7422000,14160,173600,1
2017-09-12 08:05:00,100,100,0,6365000,6835000,7341000,1075,25740,1
""".splitlines())

        bwe = self.line.csv_convert(c)
        bwj = self.line.bandwidth(bwe)
        self.line.save_new(bwj)

        self.assertEquals( len(Bandwidth.objects.all()), 4 )
