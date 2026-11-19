# Architecture Decision 001: Service Boundaries

## Status
Accepted - Initial MVP Design

## Context
We are building an E-Commerce platform using a Microservices architecture.

The goal is to establish clear business boundaries and independent ownership of data.

## Decision

The system will initially consist of six services:

### 1. User Service
- User registration
- Authentication
- User profile management

### 2. Product Catalog Service
- Product management
- Category management
- Inventory management
- Stock reservation and release

### 3. Shopping Cart Service
- Shopping cart management
- Adding and removing products
- Updating item quantities

### 4. Order Service
- Order creation
- Order lifecycle and status management
- Order history
- Order item snapshots

### 5. Payment Service
- Simulated payment processing
- Payment status management
- Payment attempts

### 6. Notification Service
- Consuming business events
- Sending order-related email notifications
- Recording notification delivery status

## Architectural Principles
- Each service owns its data.
- Services must not directly access another service's database.
- Services communicate through APIs and asynchronous messaging.
- Product prices are validated during checkout.
- Orders preserve product price snapshots.
- Inventory operations must be concurrency-safe.

## Scope Limitations
- No real payment gateway in MVP.
- No shipping service.
- No SMS integration.
- No multi-vendor marketplace.
- No multi-warehouse inventory.

## Future Considerations
Service boundaries may evolve as business requirements and domain complexity become clearer.