<?php
 echo $_SERVER['SCRIPT_NAME'];
 echo $_SERVER['SERVER_ADMIN'];
 class System {
   public $name = "SmartUmpires repo";
   public $type = "Git repository";

   public function __construct($name, $type) {
     $this->name = $name;
     $this->type = $type;
   }
 }
$SmartUmpires = new System("SmartUmpires", "SmartUmpires'System");
echo $SmartUmpires -> name;
echo $SmartUmpires -> type;

   
