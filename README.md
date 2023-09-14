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


