# forge


<h3>UML Design</h3>

+-----------------+       +-------------------+        +-------------------+
|   CarModel     |<>---->|    CarPart        |<>------| ServiceCriteria   |
+-----------------+       +-------------------+        +-------------------+
| +name: str     |       | +name: str        |        |                   |
| +add_part(part) |       |                   |        | +check_service(): |
|                 |       | +set_service_criteria()|  |   bool            |
+-----------------+       +-------------------+        +-------------------+
                         /            \
            +-------+  +-------+  +-------+
            |Engine |  |Battery|  |...    |
            +-------+  +-------+  +-------+
            | +part_name: str  |  | +part_name: str |
            | +criteria: ServiceCriteria |  | +criteria: ServiceCriteria |
            +-----------------+  +-------------------+




<h1><a href="./backend/">Directory</a></h1>

<p>

        project/
├── backend/
│   └── model/
│       ├── __init__.py
│       └── ...
├── engine/
│   └── capulet_engine.py
└── ...

</p>