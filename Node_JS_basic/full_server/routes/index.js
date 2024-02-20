import express from 'express';
import AppController from '../controllers/AppController';
import StudentsController from '../controllers/StudentsController';

function controllerRouting(app) {
  const router = express.Router();
  app.use('/', router);

  router.get('/', (request, response) => {
    AppController.getHomepage(request, response);
  });

  router.get('/students', (request, response) => {
    StudentsController.getAllStudents(request, response, process.argv[2]);
  });

  router.get('/students/:major', (request, response) => {
    StudentsController.getAllStudentsByMajor(request, response, process.argv[2]);
  });
}

export default controllerRouting;
