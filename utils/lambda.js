function generateResponse(code, body, headers = null) {
  return {
    statusCode: code,
    headers: headers || { 'Access-Control-Allow-Origin': '*' },
    body: JSON.stringify(body),
    isBase64Encoded: false,
  }
}

function response({ code, body, headers, isBase64Encoded }) {
  return {
    statusCode: code,
    headers: headers || { 'Access-Control-Allow-Origin': '*' },
    body: body,
    isBase64Encoded: !isBase64Encoded ? false : isBase64Encoded,
  }
}

module.exports = {
  generateResponse,
  response,
}
