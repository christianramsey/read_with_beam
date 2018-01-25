
# from __future__ import absolute_import

# import argparse
# import logging

import apache_beam as beam
import apache_beam.pipeline as pipeline

pipeline | beam.io.ReadFromText('data/20090629173335.plt')
