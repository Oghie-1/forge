# forge


<h3>UML Design</h3>

        +-----------------+                    +-------------------+                                     +-------------------+  
        |   CarFactory     |      <>---->         |    Car                             |<>------|           CreateModel()  |
        +-----------------+                      +-------------------+                                   +-------------------+

                                                     |       |                                                  |       |
                                                     |       |                                                  |       |
                                                        ""                                                          "
                                                        ""                                                          ""
                                                        ""                                                          ""

                                        |   service-criteria()  |                                         +-------+  +-------+  +-------+
                        
                | +criteria: ServiceCriteria(engine) |  | +criteria: ServiceCriteria(battery) |               |Engine |  |Battery|  |...    |
                                                                                                        
                                                                                                           +-------+  +-------+  +-------+
                        +-----------------+  +-------------------+
                                |                       |
                                |                       |                                                           |           |
                                                                                                                     |          |
                                                                                                         +-------+  +-------+  +-------+
                                                                                                         +check_service_criteria()

                                | +check_service(): |                 
                                                                                                        +-------+  +-------+  +-------+
                                +-------------------+                      
        
        
         | +name: str     |       
         
         
        | +name: str        |        |                   |
        | +add_part(part) |       |                   |        | +check_service(): |
        |                 |       | +set_service_criteria()|  |   bool            |
        +-----------------+       +-------------------+        +-------------------+
        
        
        
        
        
        | +name: str     |       | +name: str        |        |                   |
        | +add_part(part) |       |                   |        | +check_service(): |
        |                 |       | +set_service_criteria()|  |   bool            |
        +-----------------+       +-------------------+        +-------------------+
                                /            \
               



<h1><a href="./backend/">Directory</a></h1>

<p>

        project/
                ├── backend/
                       └── batteries/
                        └── engines
                ├── __init__.py


</p>