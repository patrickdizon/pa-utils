const pino = require('pino')
const { getEnv } = require('./env')

/**
 * Upturn logger
 *
 * Levels: { fatal: 60, error: 50, warn: 40, info: 30, debug: 20, trace: 10 }
 *
 * How to use the logger:
 *
 * Import the logger in the the main file (lambda.js | command.js)
 * which are the entry points, a correlation Id is created here
 * this represents each of the calls made to the backoffice, the child logger
 * created here should include the correlationId and
 * the logger is sent to each action were operation can be added by
 * if the action uses a service the same rule applies
 *
 * E.g.
 *
 * // action find-user.js
 * // async function findUser({ event, logger, CI }) {
 * //   const log = require('../lib/logger').child({ action: 'findUser' })
 * //   const user = userService.findUser({ userId, logger: log })
 *
 * // service user find-user.js
 * // ...
 * // const log = logger.child({ service: '' })
 */

// { name: "backoffice", operation: "actionFindUser", tag: "USER_NOT_FOUND", msg: "User id 333602382s not found","level":30,"","time":1531171074631,"msg":"hello world","pid":657,"hostname":"Davids-MBP-3.fritz.box","v":1 }

module.exports = pino({
  name: null,
  level: getEnv('LOG_LEVEL'),
  base: null,
  serializers: { error: pino.stdSerializers.err },
})
