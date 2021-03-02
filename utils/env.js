
function getEnv(name, parse) {
  if (!name) {
    throw new Error('Name should be defined in getEnv')
  }

  let val = process.env[name]

  if (!val) {
    throw new Error(`Value ${name} should exist`)
  }

  if (parse === 'bool') {
    if (val === 'true') {
      val = true
    } else if (val === 'false') {
      val = false
    } else {
      throw new Error(`Value ${val} in getEnv is not boolean parseable`)
    }
  }
  return val
}

module.exports = {
  getEnv,
}
