var PROJECT_PATH=''
var SECRET=''
var SERVER_PORT=3000
var SH_FILE=''

var http = require('http')
var spawn = require('child_process').spawn
var createHandler = require('github=webhook-handler')
var handler = createHandler({
    path:PROJECT_PATH,
    secret:SECRET
})
http.createServer(function (req, res) {
    handler(req, res, function (err) {
        res.statusCode(404);
        res.end('no such location')
    })
}).listen(SERVER_PORT)

handler.on('error', function (err) {
    console.error('ERROR:', err.message)
})

handler.on('push', function (event) {
    console.log('Received a push event for %s to %s',
        event.payload.repository.name,
        event.payload.ref)
    runCommand('sh', [SH_FILE], function (txt) {
        console.log(txt)
    })
})

function runCommand(cmd, args, callback) {
    var child = spawn(cmd, args)
    var response = ''
    child.stdout.on('data',function (buffer) {
        response += buffer.toString()
    })
    child.stdout.on('end', function () {
        callback(response)
    })
}