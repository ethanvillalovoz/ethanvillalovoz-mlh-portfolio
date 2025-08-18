# 🔍 Monitoring and Health Checks

**Date:** August 17, 2025  
**Engineer:** Ethan Villalovoz

---

## 🛠️ Goal

Implement robust monitoring solutions for the portfolio site including server monitoring with CLI tools, setting up a Prometheus/Grafana stack, and creating a dedicated DB-backed health endpoint for comprehensive system health monitoring and load testing.

---

## ✅ Tasks Completed

### 1. CLI Monitoring Tools Implementation

- Utilized key Linux monitoring tools to analyze system performance:
  - Used `top` for real-time process monitoring
  - Leveraged `vmstat` for memory and process statistics
  - Applied `iostat` to track I/O device loading and transfer rates
- Analyzed test scripts with monitoring tools to identify resource usage patterns
- Documented findings with screenshots showing CPU, memory, and I/O utilization
- Investigated script behavior using multiple terminal sessions with `tmux`
- Identified and explained why one script eventually crashed (memory exhaustion)

---

### 2. System Health Endpoint Implementation

- Created a dedicated `/health` endpoint for comprehensive system monitoring:
  ```python
  @app.route("/health")
  def health_check():
      try:
          if os.getenv("TESTING") == "true":
              cursor = mydb.execute_sql("SELECT datetime('now')")
          else:
              cursor = mydb.execute_sql("SELECT NOW()")
          result = cursor.fetchone()
          db_time = result[0] if result else None
          return jsonify({"status": "ok", "time": str(db_time)}), 200
      except Exception as e:
          return jsonify({"status": "error", "message": str(e)}), 500
  ```
- Added robust DB connection retry logic to handle startup race conditions:
  ```python
  # --- Connect with a brief retry to avoid race with DB startup ---
  if os.getenv("TESTING") == "true":
      mydb.connect(reuse_if_open=True)
  else:
      for attempt in range(30):  # up to ~60s (30 x 2s)
          try:
              mydb.connect(reuse_if_open=True)
              break
          except OperationalError as e:
              print(f"DB not ready (attempt {attempt+1}/30): {e}")
              time.sleep(2)
  ```
- Configured proper environment variables for database connection:
  ```python
  MYSQL_HOST = os.getenv("MYSQL_HOST", "mysql")   # MUST be "mysql" in docker
  MYSQL_DB   = os.getenv("MYSQL_DATABASE", "myportfoliodb")
  MYSQL_USER = os.getenv("MYSQL_USER", "myportfolio")
  MYSQL_PASS = os.getenv("MYSQL_PASSWORD", "mypassword")
  ```
- Ensured health check functionality works in both test and production environments
- Standardized error responses with appropriate HTTP status codes

---

### 3. Prometheus/Grafana Monitoring Stack Setup

- Set up comprehensive monitoring stack:
  - Installed and configured Prometheus for metrics collection
  - Set up Grafana for metric visualization and dashboards
  - Configured Node Exporter for host-level metrics
  - Added cAdvisor for container-specific monitoring
  - Implemented Alertmanager for automated notifications
- Created custom dashboard specifically for portfolio containers:
  ```yaml
  # Example Prometheus target configuration
  - job_name: 'myportfolio'
    scrape_interval: 5s
    static_configs:
      - targets: ['myportfolio:5000']
        labels:
          service: 'portfolio-app'
  ```
- Tracked key performance metrics across all system components:
  - CPU usage per container (nginx, mysql, myportfolio)
  - Memory utilization across the stack
  - Network I/O for request handling
  - Database query performance
- Configured proper service dependencies in Docker Compose:
  ```yaml
  # Enhanced Docker Compose configuration
  myportfolio:
    container_name: myportfolio
    build: .
    restart: always
    env_file:
      - .env
    depends_on:
      mysql:
        condition: service_healthy
  ```
- Added MySQL health check to ensure database readiness:
  ```yaml
  healthcheck:
    # Wait until the DB accepts connections with the app user/password.
    test: ["CMD-SHELL", "mariadb-admin ping -h 127.0.0.1 -p$MARIADB_PASSWORD --silent || exit 1"]
    interval: 5s
    timeout: 3s
    retries: 20
  ```

---

### 4. Load Testing and Performance Analysis

- Conducted load testing with Apache Bench to simulate high traffic:
  ```bash
  ab -n 1000 -c 10 https://ethanvillalovoz.duckdns.org/
  ```
- Analyzed performance metrics during load testing:
  - Observed NGINX handling most of the concurrent connections
  - Identified MySQL as the bottleneck during high query volumes
  - Noted myportfolio container scaling with increased requests
- Created additional load tests targeting the health endpoint:
  ```bash
  ab -n 1000 -c 10 https://ethanvillalovoz.duckdns.org/health
  ```
- Captured baseline metrics for normal operation versus peak load
- Documented performance insights with Grafana dashboard screenshots
- Identified areas for potential performance optimization

---

## Challenges Faced

- **Memory Issues During Monitoring**: Initial monitoring attempts consumed excessive resources
  - Resolved by properly configuring Prometheus scrape intervals
  - Optimized Docker container memory limits
  
- **Database Connection Reliability**: Health check initially failed intermittently
  - Implemented retry mechanism with exponential backoff
  - Added proper error handling and logging
  - Created connection pooling for improved stability
  
- **Docker Compose Configuration**: Services initially started in wrong order
  - Implemented proper `depends_on` conditions
  - Added health checks to ensure services only start when dependencies are ready
  - Configured environment variables consistently across containers
  
- **Grafana Dashboard Configuration**: Initial metrics collection was overwhelming
  - Created focused dashboard for only the three main services
  - Applied filtering to reduce noise and focus on actionable metrics
  - Set up appropriate time ranges for meaningful trend analysis
  
- **Load Testing Impact**: First load tests crashed the application
  - Adjusted concurrency levels for realistic testing
  - Implemented gradual load increase to identify breaking points
  - Created separate tests for different endpoints to isolate bottlenecks

---

## 🧠 Skills Practiced

- System monitoring with CLI tools (top, vmstat, iostat)
- Application health check endpoint implementation
- Database connection management and error handling
- Docker container health checks and dependency management
- Prometheus metrics configuration and collection
- Grafana dashboard creation and customization
- Load testing with Apache Bench
- Performance analysis and bottleneck identification
- Environment variable configuration for containerized applications
- JSON response formatting for API endpoints
- Exception handling for robustness
- Connection retry patterns for reliability

---

## 📌 Notes for Resume or LinkedIn

- Implemented comprehensive monitoring solution using Prometheus and Grafana for containerized Flask application
- Created DB-backed health endpoint with retry logic for reliable system status monitoring
- Designed container-specific Grafana dashboards to track performance metrics across web server, application, and database
- Conducted load testing and performance analysis to identify system bottlenecks and optimize resource allocation
- Improved application reliability through proper Docker health checks and dependency management
