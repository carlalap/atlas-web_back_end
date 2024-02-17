// 1. Using Process stdin
// program where user should be able
// to input their name on a new line
process.stdin.setEncoding('utf-8');
process.stdout.write('Welcome to Holberton School, what is your name?\n');
process.stdin.once('readable', () => {
  const name = process.stdin.read();
  if (name) process.stdout.write(`Your name is: ${name}`);
});

process.stdin.once('end', () => {
  process.stdout.write('This important software is now closing\n');
});
