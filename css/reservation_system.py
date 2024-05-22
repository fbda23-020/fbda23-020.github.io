sequenceDiagram
    participant Customer as "Customer"
    participant WebApp as "Web Application"
    participant ReservationSystem as "Reservation System"
    participant PaymentGateway as "Payment Gateway"
    participant HotelDB as "Hotel Database"

    note "Customer initiates online booking"
    Customer->>WebApp: Book Room
    WebApp->>ReservationSystem: Check Room Availability
    ReservationSystem->>HotelDB: Get Room Details
    HotelDB->>ReservationSystem: Room Details
    ReservationSystem->>WebApp: Room Availability
    WebApp->>Customer: Room Availability

    note "Customer selects room and proceeds to payment"
    Customer->>WebApp: Select Room and Proceed to Payment
    WebApp->>ReservationSystem: Create Reservation
    ReservationSystem->>HotelDB: Save Reservation
    HotelDB->>ReservationSystem: Reservation ID
    ReservationSystem->>WebApp: Reservation ID
    WebApp->>Customer: Reservation ID

    note "Customer makes payment"
    Customer->>PaymentGateway: Make Payment
    PaymentGateway->>ReservationSystem: Payment Confirmation
    ReservationSystem->>HotelDB: Update Reservation Status
    HotelDB->>ReservationSystem: Updated Reservation Status

    note "System checks for payment within 3 days"
    ReservationSystem->>HotelDB: Get Reservation Details
    HotelDB->>ReservationSystem: Reservation Details
    ReservationSystem->>ReservationSystem: Check Payment Status
    alt Payment not made within 3 days
        ReservationSystem->>HotelDB: Cancel Reservation
        HotelDB->>ReservationSystem: Reservation Cancelled
    end