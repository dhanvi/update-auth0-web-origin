# update auth0 web origin

Github action to update auth0 web origin update auth0 web origin

## Usage

Requires the below environment variables
```
AUTH0_TOKEN
CLIENT_ID
CLIENT_HOST
WEB_ORIGIN_DOMAIN
ACTION_TYPE
```

### Sample workflow

```yaml
jobs:
  example:
    runs-on: ubuntu-latest
    steps:
    - name: example
      uses: dhanvi/update-auth0-web-origin@master
      env:
        AUTH0_TOKEN: ${{ secrets.AUTH0_TOKEN }}
        CLIENT_ID: "11111"
        CLIENT_HOST: "example.auth0.com"
        WEB_ORIGIN_DOMAIN: "example.com"
        ACTION_TYPE: "add"
```

