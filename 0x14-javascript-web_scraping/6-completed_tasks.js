#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) console.error(error);
  if (response && response.statusCode === 200) {
    const tasks = JSON.parse(body);
    const completedTasks = {};
  
    for (const task of tasks) {
      if (task.completed) {
        if (completedTasks[task.userId] === undefined) {
          completedTasks[task.userId] = 1;
        } else {
          completedTasks[task.userId] += 1;
        }
      }
    }
    console.log(completedTasks)
  }
});
