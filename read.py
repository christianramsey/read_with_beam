
# from __future__ import absolute_import

# import argparse
# import logging

import apache_beam as beam
import apache_beam.pipeline as pipeline
from apache_beam.options.pipeline_options import PipelineOptions


# What > Remove the first four lines
# Where > Within a single implicit global event-time window
# When > Once, when the entire bounded input source has been consumed
# How > Not relevant


p = beam.Pipeline(options=PipelineOptions())
lines = p | 'ReadMyFile' >> beam.io.ReadFromText('/Users/cramsey/Documents/Distributed Deep Learning/Reading Data/beam_read/read_with_beam/data/data.csv')

lines | 'WriteMyFile' >> beam.io.WriteToText(
      'beam_data/outputData.csv')

p.run()
lines




