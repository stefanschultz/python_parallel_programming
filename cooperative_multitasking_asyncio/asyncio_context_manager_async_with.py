import asyncio


class AsyncDatabaseConnection:
    """An asynchronous context manager to simulate a database connection."""

    def __init__(self, database_name):
        self.database_name = database_name

    async def connect(self):
        """Simulate an asynchronous connection to a database."""
        await asyncio.sleep(1)  # Simulate the connection time
        print(f"Connected to {self.database_name} database.")

    async def disconnect(self):
        """Simulate closing the database connection asynchronously."""
        await asyncio.sleep(1)  # Simulate the disconnection time
        print(f"Disconnected from {self.database_name} database.")

    async def __aenter__(self):
        """Enter the runtime context related to this object."""
        await self.connect()
        return self  # Return an instance of the connection

    async def __aexit__(self, exc_type, exc, tb):
        """Exit the runtime context and close the connection."""
        await self.disconnect()


async def main():
    # Use the asynchronous context manager to manage a database connection
    async with AsyncDatabaseConnection("MyDatabase") as db:
        print("Performing operations with the database...")

# Execute the main function to see the context manager in action
asyncio.run(main())
