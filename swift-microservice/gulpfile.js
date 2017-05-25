'use strict';

var gulp = require('gulp');
var child = require('child_process')

var server = null;

gulp.task('develop', ['compile:swift','run:server','watch']);

gulp.task('watch', function() {
    gulp.watch('./Sources/**/*.swift', ['compile:swift','run:server']);
});

gulp.task('compile:swift', function() {
    return child.spawnSync('swift', ['build'], {
    })
});

gulp.task('run:server', function() {
    if (server) 
        server.kill();
    server = child.spawn('./Server', [], {
        cwd: '.build/debug'
    });
    server.stderr.on('data', function(data) {
        process.stdout.write(data.toString());
    });
});

gulp.task('default', ['compile:swift']);