const express = require('express');
const app = express();
const port = 9100; // Porta padrão do Node Exporter

// Importe o módulo Faker.js
const faker = require('faker');

// Rota para métricas gerais
app.get('/metrics/general', (req, res) => {
  // Gere métricas gerais fictícias
  const totalRequests = faker.random.number();
  const totalConnections = faker.random.number();
  const acceptedConnections = faker.random.number();
  const droppedConnections = faker.random.number();
  const activeConnections = faker.random.number();

  // Formate as métricas no formato do Node Exporter
  const metrics = `
    # Métricas Gerais Simuladas
    nginx_http_requests_total ${totalRequests}
    nginx_http_connections_total ${totalConnections}
    nginx_http_accepted_connections_total ${acceptedConnections}
    nginx_http_dropped_connections_total ${droppedConnections}
    nginx_http_active_connections ${activeConnections}
  `;

  res.set('Content-Type', 'text/plain');
  res.send(metrics);
});

// Rota para métricas de cache
app.get('/metrics/cache', (req, res) => {
  // Gere métricas de cache fictícias
  const cacheHits = faker.random.number();
  const cacheMisses = faker.random.number();
  const cacheStale = faker.random.number();
  const cacheRevalidated = faker.random.number();

  // Formate as métricas no formato do Node Exporter
  const metrics = `
    # Métricas de Cache Simuladas
    nginx_http_cache_hits_total ${cacheHits}
    nginx_http_cache_misses_total ${cacheMisses}
    nginx_http_cache_stale_total ${cacheStale}
    nginx_http_cache_revalidated_total ${cacheRevalidated}
  `;

  res.set('Content-Type', 'text/plain');
  res.send(metrics);
});

app.listen(port, () => {
  console.log(`Servidor Node Exporter Simulado em execução na porta ${port}`);
});
