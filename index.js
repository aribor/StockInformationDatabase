const express = require('express')
const { spawn } = require('child_process');
const app = express()
const port = 3000

app.get('/', (req, res) => {
    var dataToSend;
    // spawn new child process to call python script
    const python = spawn('python', ['datarequest.py']);
    //collect data from script
    python.stdout.on('data', function (data) {
        console.log('Pipe data from python script ...');
        dataToSend = data.toString();

    });

    // in close event, stream from child process is closed

    python.on('close', (code) => {
        console.log('child process close all stdio with code ${code}');
        res.send(dataToSend)
    });

});

app.listen(port, () => console.log('example app listening on port ${port}!'))
