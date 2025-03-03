const express = require('express');
const app = express();
const port = process.env.PORT || 3000;
const neo4j = require('neo4j-driver').v1;
const driver = neo4j.driver('bolt://localhost:7687', neo4j.auth.basicAuth('neo4j', 'jiayi031220'));
const fs = require('fs');
const path = require('path');
const openpyxl = require('openpyxl');

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

function importDataFromExcel() {
  const workbook = openpyxl.read(fs.readFileSync(path.join(__dirname, 'Triple.xlsx')));
  const booksheet = workbook.worksheets[0];
  let i = 1;
  const session = driver.session();

  session.writeTransaction(tx => {
    return tx.run('MATCH (n) DETACH DELETE n'); 
  });

  const loop = true;
  while (loop) {
    i += 1;
    if (i > 218488) break; // 取前1000行数据

    const entity_1 = booksheet.getCell(i, 1).value;
    if (entity_1 === null) {
      loop = false;
      break;
    }

    const relation_data = booksheet.getCell(i, 2).value;
    const entity_2 = booksheet.getCell(i, 3).value;

    return session.writeTransaction(tx => {
      const entity_node_1 = { labels: ['patent'], properties: { name: entity_1 } };
      const entity_node_2 = { labels: ['patent'], properties: { name: entity_2 } };

      const createNodesAndRelationship = `
        MERGE (n1:patent {name: $entity_1})
        MERGE (n2:patent {name: $entity_2})
        CREATE (n1)-[:${relation_data}]->(n2)
      `;

      return tx.run(createNodesAndRelationship, { entity_1, entity_2 });
    });
  }

  session.close();
}

// 在服务器启动时导入数据
importDataFromExcel();

// Endpoint for /searchEntity
app.get('/searchEntity', async (req, res) => {
  const entity_name = req.query.entity_name;

  try {
    const session = driver.session();
    const result = await session.readTransaction(async tx => {
      const query = `
        MATCH (n)-[r]->(m) WHERE n.name = $entity_name
        RETURN n, r, m
      `;
      const data = await tx.run(query, { entity_name: entity_name });

      return data.records.map(record => ({
        node: record._fields[0].properties,
        relation: record._fields[1].type,
        target: record._fields[2].properties
      }));
    });
    session.close();

    res.json(result);
  } catch (error) {
    console.error(error);
    res.status(500).send('Internal Server Error');
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});