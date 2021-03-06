#! /usr/bin/env python

import sys
import logging
import logging.handlers

try:
  import config.setupdatabaseconfig as configModule
except ImportError:
  import setupdatabaseconfig as configModule

import socorro.database.schema as socorro_schema
import socorro.lib.ConfigurationManager as configurationManager
import socorro.lib.util as sutil

try:
  config = configurationManager.newConfiguration(configurationModule=configModule, applicationName="Socorro Database Setup 1.0")
except configurationManager.NotAnOptionError, x:
  print >>sys.stderr, x
  print >>sys.stderr, "for usage, try --help"
  sys.exit()

logger = logging.getLogger("setupDatabase")
logger.setLevel(logging.DEBUG)

sutil.setupLoggingHandlers(logger, config)
sutil.echoConfig(logger, config)

try:
  socorro_schema.setupDatabase(config, logger)
finally:
  logger.info("done.")


