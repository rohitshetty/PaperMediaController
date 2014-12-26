int tags[3]={0,0,0}; //It turns the reading from analog sensor are  not stable so to debounce it we use this 
void setup(){
 Serial.begin(9600); //to Bluetooth HC05
  
}
void loop(){

//*Serial.println(analogRead(A2));
if(analogRead(A0) < 200 && tags[0]==0){
Serial.println("p"); //This makes sure play seqeunce is fired only once 
tags[0]=1;
}
 if (analogRead(A0) > 500 && tags[0]==1){
 tags[0]=0; //Reset once it crosses 500
 }
 
 if(analogRead(A1) < 200 && tags[1]==0){
Serial.println("l"); //Last song
tags[1]=1;
}
 if (analogRead(A1) > 500 && tags[1]==1){
 tags[1]=0;
 }
 
 
  if(analogRead(A2) < 100 && tags[2]==0){
Serial.println("n"); //Next Song
tags[2]=1;
}
 if (analogRead(A2) > 500 && tags[2]==1){
 tags[2]=0;
 }
  

}
