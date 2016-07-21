 int LEDPIN=7;
 int LEDPIN2=8;
 int BUTTON=10;
      
void setup() {
  pinMode(LEDPIN,OUTPUT);
  pinMode(LEDPIN2,OUTPUT);
  pinMode(BUTTON,INPUT_PULLUP);


}

void loop() {
  if(digitalRead(BUTTON)==LOW){
    while(digitalRead(BUTTON)==HIGH){
      
   
      for(int i = 0; i < 6; i++){
        
    
        digitalWrite(LEDPIN,HIGH);
        delay(300);
        digitalWrite(LEDPIN,LOW);
        delay(100);
        digitalWrite(LEDPIN,HIGH);
        delay(300);
        digitalWrite(LEDPIN,LOW);
        delay(100);
        digitalWrite(LEDPIN2,HIGH);
        delay(300);
        digitalWrite(LEDPIN2,LOW);
        delay(150);
        digitalWrite(LEDPIN2,HIGH);
        delay(200);
        digitalWrite(LEDPIN2,LOW);
        delay(150);
        digitalWrite(LEDPIN,HIGH);
        delay(300);
        digitalWrite(LEDPIN,LOW);
        delay(100);
        digitalWrite(LEDPIN,HIGH);
        delay(300);
        digitalWrite(LEDPIN,LOW);
        delay(150);
        digitalWrite(LEDPIN2,HIGH);
        delay(300);
        digitalWrite(LEDPIN2,LOW);
        delay(500);
      }
      delay(3000);
    }
   

  }

    
}
  
