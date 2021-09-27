SIMPLE_STRING = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''

NESTED_STRUCTURE = '''{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow:
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}'''

PLAIN_STRUCTURE = '''Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]'''


JSON_STRUCTURE = '''{
  "common": {
    "condition": "nested",
    "value": {
      "follow": {
        "condition": "added",
        "value": false
      },
      "setting1": {
        "condition": "unchanged",
        "value": "Value 1"
      },
      "setting2": {
        "condition": "deleted",
        "value": 200
      },
      "setting3": {
        "condition": "changed",
        "value": {
          "new_value": null,
          "old_value": true
        }
      },
      "setting4": {
        "condition": "added",
        "value": "blah blah"
      },
      "setting5": {
        "condition": "added",
        "value": {
          "key5": "value5"
        }
      },
      "setting6": {
        "condition": "nested",
        "value": {
          "doge": {
            "condition": "nested",
            "value": {
              "wow": {
                "condition": "changed",
                "value": {
                  "new_value": "so much",
                  "old_value": ""
                }
              }
            }
          },
          "key": {
            "condition": "unchanged",
            "value": "value"
          },
          "ops": {
            "condition": "added",
            "value": "vops"
          }
        }
      }
    }
  },
  "group1": {
    "condition": "nested",
    "value": {
      "baz": {
        "condition": "changed",
        "value": {
          "new_value": "bars",
          "old_value": "bas"
        }
      },
      "foo": {
        "condition": "unchanged",
        "value": "bar"
      },
      "nest": {
        "condition": "changed",
        "value": {
          "new_value": "str",
          "old_value": {
            "key": "value"
          }
        }
      }
    }
  },
  "group2": {
    "condition": "deleted",
    "value": {
      "abc": 12345,
      "deep": {
        "id": 45
      }
    }
  },
  "group3": {
    "condition": "added",
    "value": {
      "deep": {
        "id": {
          "number": 45
        }
      },
      "fee": 100500
    }
  }
}'''
