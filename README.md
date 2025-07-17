# ALX Backend Caching - Property Listings

A Django project demonstrating Redis caching strategies for property listings, including view caching, queryset caching, and cache invalidation.

## Features

- **Dockerized Infrastructure**:
  - PostgreSQL database
  - Redis cache server
- **Caching Strategies**:
  - View-level caching with `@cache_page`
  - Low-level queryset caching
  - Automatic cache invalidation using signals
- **Monitoring**:
  - Redis cache hit/miss metrics
  - Hit ratio calculation

## Prerequisites

- Docker and Docker Compose
- Python 3.8+
- pip

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/alx-backend-caching_property_listings.git
   cd alx-backend-caching_property_listings