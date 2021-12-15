<?php
class Tiger{
    public $string;
    protected $var;
    public function __toString(){
        return $this->string;
    }
    public function boss($value){
        @eval($value);
    }
    public function __invoke(){
        $this->boss($this->var);
    }
}

class Lion{
    public $tail;
    public function __construct(){
        $this->tail = array();
    }
    public function __get($value){
        $function = $this->tail;
        return $function();
    }
}


class Monkey{
    public $head;
    public $hand;
    public function __construct($here="Zoo"){
        $this->head = $here;
        echo "Welcome to ".$this->head."<br>";
    }
    public function __wakeup(){
        if(preg_match("/gopher|http|file|ftp|https|dict|\.\./i", $this->head)) {
            echo "hacker";
            $this->source = "index.php";
        }
    }
}

class Elephant{
    public $nose;
    public $nice;
    public function __construct($nice="nice"){
        $this->nice = $nice;
        echo $nice;
    }
    public function __toString(){
        return $this->nice->nose;
    }
}

if(isset($_POST['zoo'])){
    @unserialize($_POST['zoo']);
}
else{
    $a = new Monkey;
    echo "hint in hint.php!";
}
?>