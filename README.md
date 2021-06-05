# aiophotoprism

Asynchronous Python client for the [Photoprism](https://photoprism.app/)

**Warning**: [Photoprism API](https://docs.photoprism.org/developer-guide/frontend/rest-api/) is not stable yet,
use on your own risk

NOTE: The package is in active development. _Not all features of the API are implemented._

## Installation

`pip install aiophotoprism`

## Usage

```python
import asyncio

from aiophotoprism import Photoprism

async def main():

  async with Photoprism("username", "password") as client:
    # interact with the client here
    pass

if __name__ == "__main__":
  asyncio.run(main())
```

### Photoprism

Photoprism is the entrypoint class, it acts as an async context manager and provides access to API endpoints.

#### Initialization

```python
    def __init__(
        self,
        username, # your username
        password, # your password
        url="http://127.0.0.1:2342", # A base URL of the server, https://photoprism.example.com:443/something is also possible
        timeout=DEFAULT_TIMEOUT, # Timeout in seconds
        verify_ssl=True, # Perform SSL verification
        loop=None, # event loop
        session=None # client session,
    )...
```

#### Photos

Returns list of photos.

```python
await client.photos(count=50)
```

#### Config

Returns Photoprism instance config.

```python
await client.config()
```

#### Index

Forces the Photoprism instance to index photos. Complete scan is not supported.

```python
await client.index()
```

## License

MIT License

Copyright (c) 2021 Gleb Sinyavskiy

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
