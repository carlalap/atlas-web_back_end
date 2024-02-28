import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

// Array with the list of products:

const listProducts = [
    { Id: 1, name: 'Suitcase 250', price: 50, stock: 0 },
    { Id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
    { Id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
    { Id: 4, name: 'Suitcase 1050', price: 550, stock: 15 }
  ]

// Data Access : return the item from listProducts with the same id
function getItemById(id) {
   return listProducts.filter((item) => item.itemId === id)[0];
} 

// Create a client to connect to the Redis server:

const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

function reserveStockById(itemId, stock) {
  client.set(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
  const stock = await getAsync(`item.${itemId}`);
  return stock;
}

// express server listening on the port 1245

const app = express();
const port = 1245;

const prodStatus = {status: 'Product not found'};


app.get('/list_products', (request, response) => {
    response.json(listProducts);
  });
  
app.get('/list_products/:itemId', async (request, response) => {
    const itemId = Number(request.params.itemId);
    const item = getItemById(itemId)

    if (!item) {
        response.json(prodStatus);
        return;
    }

    const currentStock = await getCurrentReservedStockById(itemId);
    const stock =
      currentStock !== null ? currentStock : item.initialAvailableQuantity;

    item.currentQuantity = stock;
    response.json(item);
});

app.get('/reserve_product/:itemId', async (request, response) => {
    const itemId = Number(request.params.itemId);
    const item = getItemById(itemId)
    // is there at least one stock available?
    const noProduct = { status: 'Not enough stock available', itemId };

    if (!item) {
        response.json(prodStatus);
        return;
    }

    let currentStock = await getCurrentReservedStockById(itemId);
    if (currentStock === null) currentStock = item.initialAvailableQuantity;
  
    if (currentStock <= 0) {
      response.json(noStock);
      return;
    }

    reserveStockById(itemId, Number(currentStock) - 1);

    res.json(reservationConfirmed);
});


app.listen(port, (error) => { // Start the server and listen on the specified port
    if (error) { // If an error occurs while starting the server
      console.log('Something went wrong', error); // Log the error message
    } else { // If the server starts successfully
      console.log(`Server is listening on port ${port}`); // Log a message indicating that the server is listening on the specified port
    }
  });
