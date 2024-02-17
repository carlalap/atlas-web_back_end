// 1. Using Process stdin
// program where user should be able
// to input their name on a new line
console.log('Welcome to Holberton School, what is your name?')
process.stdin.once('data', (data) => {
    const name = data.toString().trim();
    console.log(`Your name is: ${name}`);
    console.log('This important software is now closing');
});
