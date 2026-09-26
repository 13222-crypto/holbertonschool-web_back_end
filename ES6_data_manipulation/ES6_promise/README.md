# ES6 Promises

## Description
This project focuses on asynchronous JavaScript concepts using ES6 Promises, async/await syntax, handling errors with try/catch, and executing multiple concurrent promises.

## Learning Objectives
- Promises (how, why, and what)
- Using `.then()`, `.catch()`, and `.finally()` methods
- Working with `Promise.all()`, `Promise.allSettled()`, and `Promise.race()`
- Error handling using `throw` and `try / catch`
- Using `async` functions and the `await` operator

## Requirements
- Executed on **Ubuntu 20.04 LTS** using **Node.js 20.x.x**
- Tested using **Jest** (`npm run test`)
- Verified against **ESLint** code formatting guidelines (`npm run lint`)

## Tasks Directory

| File | Description |
| --- | --- |
| `0-promise.js` | Returns a basic Promise using `getResponseFromAPI()`. |
| `1-promise.js` | Returns a resolved or rejected Promise based on a boolean parameter. |
| `2-then.js` | Appends handlers to a Promise to update response state and log output. |
| `3-all.js` | Resolves multiple promises concurrently with `Promise.all()`. |
| `4-user-promise.js` | Returns a resolved promise containing user credentials. |
| `5-photo-reject.js` | Returns a rejected promise with an Error. |
| `6-final-user.js` | Uses `Promise.allSettled()` to return status of user creation and photo upload. |
| `7-load_balancer.js` | Returns the fastest resolving promise using `Promise.race()`. |
| `8-try.js` | Function that throws an error when dividing by zero. |
| `9-try.js` | Creates a guardrail wrapper queue with `try/catch/finally`. |
| `100-await.js` | Uses `async/await` to call multiple functions safely. |

## Author
Johann Kerbrat, Engineering Manager at Uber Works
