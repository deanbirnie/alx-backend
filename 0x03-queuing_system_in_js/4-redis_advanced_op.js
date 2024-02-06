import redis, { createClient } from 'redis';

const client = createClient();

client.on('error', (err) => console.log('Redis client not connected to the server:', err.toString()));
client.on('connect', () => console.log('Redis client connected to the server'));

const keyValues = {
  Portland: 50,
  Seattle: 80,
  'New York': 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2,
};

for (const [key, value] of Object.entries(keyValues)) {
  client.hset('HolbertonSchools', key, value, redis.print);
}

client.hgetall('HolbertonSchools', (err, reply) => {
  if (err) {
    console.error(err);
  } else {
    console.log(reply);
  }
});
