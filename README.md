# link-khovanov

Compute distinct Khovanov values over all component orientations.

## Installation

```bash
pip install link-khovanov
```

## Quick start

`from link_khovanov import link_khovanov` then `link_khovanov(pd_code)`.

PD codes are lists of four-entry crossings. Each arc label must occur exactly twice. Functions validate their inputs and do not mutate caller-owned PD-code lists unless explicitly documented.

## Development

Use Python 3.10 or newer for Python packages. Build distributions with `poetry build`. Run the package's tests or examples before publishing. C++ projects require a modern standards-compliant compiler.

## License

MIT. See `LICENSE`.
