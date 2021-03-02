function isNumeric(n) {
  // eslint-disable-next-line no-restricted-globals
  return !isNaN(parseFloat(n)) && isFinite(n)
}

function compare(a, b, comparisonFields) {
  const changes = []
  comparisonFields.map(field => {
    const oldElement =
      a[field] instanceof Date ? a[field].toISOString() : a[field]
    const newElement =
      b[field] instanceof Date ? b[field].toISOString() : b[field]
    if (isNumeric(oldElement) && isNumeric(newElement)) {
      const difference = newElement - oldElement
      if (difference !== 0) {
        changes.push({ field, oldElement, newElement })
      }
    } else if (Array.isArray(oldElement) && Array.isArray(newElement)) {
      if (oldElement.toString() !== newElement.toString()) {
        changes.push({ field, oldElement, newElement })
      }
    } else if (oldElement !== newElement) {
      changes.push({ field, oldElement, newElement })
    }
    return true
  })
  return changes
}

function is2xx(statusCode) {
  return statusCode >= 200 && statusCode <= 299
}

function isNot2xx(statusCode) {
  return !is2xx(statusCode)
}

module.exports = {
  compare,
  is2xx,
  isNot2xx,
}
