import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();
// Promisify Redis commands
const getAsync = promisify(client.get).bind(client);

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err.message}`);
});

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
    const response = await getAsync(schoolName);
    console.log(response);
}
  
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
