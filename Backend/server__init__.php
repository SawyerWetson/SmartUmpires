<?php
echo $_SERVER['SCRIPT_NAME'] . "<br>";
echo (isset($_SERVER['SERVER_ADMIN']) ? $_SERVER['SERVER_ADMIN'] : '') . "<br>";

class System {
  public $name = "SmartUmpires repo";
  public $type = "Git repository";

  public function __construct($name, $type) {
    $this->name = $name;
    $this->type = $type;
  }
}

$SmartUmpires = new System("SmartUmpires", "SmartUmpires System");
echo $SmartUmpires->name . "<br>";
echo $SmartUmpires->type . "<br>";
