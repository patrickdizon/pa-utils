function pluralize(value, cases = []) {
  for (let i = cases.length; cases.length < 4; i++) {
    cases.push(
      i === 3 ? null : '',
    )
  }
  if (value) {
    if (value === 0) {
      return cases[0]
    }

    if (value === 1) {
      return cases[1]
    }

    if (value > 1) {
      return cases[2]
    }
  } else {
    if (cases[3]) {
      return cases[3]
    } else {
      return cases[0]
    }
  }
  return ''
}

module.exports = {
  pluralize,
}
