/*
 * Copyright (C) 2016 TopCoder Inc., All Rights Reserved.
 */
'use strict';
/**
 * Implement drones API contract
 *
 * @author      TSCCODER
 * @version     1.0
 */

const request = require('request-promise');
const config = require('config');

module.exports = {
  getAll,
  update,
};

function* getAll() {
  const url = `${config.api.basePath}/api/v1/drones`;
  return yield request({ url, json: true });
}

function* update(id, payload) {
  const url = `${config.api.basePath}/api/v1/drones/${id}`;
  return yield request({
    url,
    method: 'PUT',
    body: payload,
    json: true,
  });
}
