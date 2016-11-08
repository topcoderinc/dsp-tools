/*
 * Copyright (C) 2016 TopCoder Inc., All Rights Reserved.
 */
'use strict';
/**
 * Run the benchmark for drones update API to test the update position on map
 *
 * @author      TSCCODER
 * @version     1.0
 */

global.Promise = require('bluebird');
const winston = require('winston');
const co = require('co');
const apiTester = require('./ApiTester');
const sleep = require('sleep');
const config = require('config');

/**
 * Get a random point between min and max coordinates
 * @param  {Number}     from           the max degree
 * @param  {Number}     to             the min degree
 * @param  {Number}     fixed          the fixed decimal points
 */
function getRandomPoint(from, to, fixed) {
  return (Math.random() * (to - from) + from).toFixed(fixed) * 1;         // eslint-disable-line no-mixed-operators
}

co(function* () {
  winston.info('get a list of all the drones');
  const drones = yield apiTester.getAll();
  winston.info(`${drones.length} drones found`);
  const flag = true;
  // hit update api
  while (flag === true) {
    const index = Math.floor(Math.random() * (9999 - 0 + 1)) + 0;          // eslint-disable-line no-mixed-operators
    const drone = drones[index];
    const lat = getRandomPoint(-90, 90, 6);
    const lng = getRandomPoint(-180, 180, 6);
    winston.info(`updating location of ${drone.id}`);
    yield apiTester.update(drone.id, {
      lat,
      lng,
    });
    sleep.sleep(config.wait);
  }

  winston.info('exiting benchmark');
}).then(() => {
  winston.info('Done');
  process.exit();
}).catch((e) => {
  winston.error(e);
  process.exit();
});
