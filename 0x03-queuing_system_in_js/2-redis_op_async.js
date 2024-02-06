import redis, { createClient } from 'redis';
import { promisify } from 'util';

const client = createClient();
const getAsync = promisify(client.get).bind(client);

client.on('error', (err) => console.log('Redis client not connected to the server:', err.toString()));
client.on('connect', () => console.log('Redis client connected to the server'));

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, redis.print);
};

const displaySchoolValue = async (schoolName) => {
  try {
    const reply = await getAsync(schoolName);
    console.log(reply);
  } catch (err) {
    console.error(err);
  }
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
