const int lowerLayerPin = 2;
const int upperLayerPin = 3;
const int lifterPin = 4;
const int diskMotorPin= 12;

const int lowerLayerDirPin = 5;
const int upperLayerDirPin = 6;
const int lifterDirPin = 7;
const int diskMotorDirPin = 13;

const int lowerLayerHomingPin = 9;
const int upperLayerHomingPin = 10;
const int lifterHomingPin = 11;

bool lowerLayerHomed = false;
bool upperLayerHomed = false;
bool lifterHomed = false;


void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);
  
  pinMode(lowerLayerPin,OUTPUT); 
  pinMode(upperLayerPin,OUTPUT);
  pinMode(lifterPin,OUTPUT);
  pinMode(diskMotorPin,OUTPUT);
  
  pinMode(lowerLayerDirPin,OUTPUT);
  pinMode(upperLayerDirPin,OUTPUT);
  pinMode(lifterDirPin,OUTPUT);
  pinMode(diskMotorDirPin,OUTPUT);

  pinMode(lowerLayerHomingPin, INPUT_PULLUP);
  pinMode(upperLayerHomingPin, INPUT_PULLUP);
  pinMode(lifterHomingPin, INPUT_PULLUP);

  homeElement("lowerLayer");
  homeElement("upperLayer");
  homeElement("lifter");
}

void loop() {
  while(!Serial.available());
  String rxString = "";
  String strArr[3]; //Set the size of the array to equal the number of values you will be receiveing.
  //Keep looping until there is something in the buffer.
  while (Serial.available()) {
    //Delay to allow byte to arrive in input buffer.
    delay(2);
    //Read a single character from the buffer.
    char ch = Serial.read();
    //Append that single character to a string.
    rxString+= ch;
  }

  if(rxString == "homeElements"){
    homeElement("lowerLayer");
    homeElement("upperLayer");
    homeElement("lifter");      
  }
  
  else{
  
    int stringStart = 0;
    int arrayIndex = 0;
    for (int i=0; i < rxString.length(); i++){
      //Get character and check if it's our "special" character.
      if(rxString.charAt(i) == ','){
        //Clear previous values from array.
        strArr[arrayIndex] = "";
        //Save substring into array.
        strArr[arrayIndex] = rxString.substring(stringStart, i);
        //Set new string starting point.
        stringStart = (i+1);
        arrayIndex++;
      }
    }
    //Put values from the array into the variables.
    String element = strArr[0];
    String dir = strArr[1];
    String steps = strArr[2];
  
    int dirInt = dir.toInt();
    int stepsInt = steps.toInt();
  
    Serial.println(element);
    Serial.println(dirInt);
    Serial.println(steps);
  
    moveElement(element, dirInt, stepsInt);
  }
}

void moveElement(String element, int dirInt, int stepsInt){
  int elementPin;
  int elementDirPin;
  int transformedSteps = stepsInt * 20;
  
  if(element == "lowerLayer"){
    elementPin = lowerLayerPin;  
    elementDirPin = lowerLayerDirPin;  
  }   
  else if(element == "upperLayer"){
    elementPin = upperLayerPin;
    elementDirPin = upperLayerDirPin; 
  }   
  else if(element == "lifter"){
    elementPin = lifterPin;  
    elementDirPin = lifterDirPin;
  }
  else if(element == "diskMotor"){
    elementPin = diskMotorPin;  
    elementDirPin = diskMotorDirPin;
  }

  Serial.println(elementPin);
  Serial.println(elementDirPin);
  digitalWrite(elementDirPin, dirInt);

   for(int x = 0; x < transformedSteps; x++) {
     digitalWrite(elementPin,HIGH); 
     delayMicroseconds(1000); 
     digitalWrite(elementPin,LOW); 
     delayMicroseconds(1000); 
   }
  
}


void homeElement(String element){
  int elementPin;
  int elementDirPin;
  int elementHomingPin;
  
  if(element == "lowerLayer"){
    elementPin = lowerLayerPin;  
    elementDirPin = lowerLayerDirPin;
    digitalWrite(elementDirPin, 0);
    elementHomingPin = lowerLayerHomingPin;
  }   
  else if(element == "upperLayer"){
    elementPin = upperLayerPin;
    elementDirPin = upperLayerDirPin;
    digitalWrite(elementDirPin, 1);
    elementHomingPin = upperLayerHomingPin;
  }   
  else if(element == "lifter"){
    elementPin = lifterPin;  
    elementDirPin = lifterDirPin;
    digitalWrite(elementDirPin, 0);
    elementHomingPin = lifterHomingPin;
  }


  while(digitalRead(elementHomingPin)){
    digitalWrite(elementPin,HIGH); 
    delayMicroseconds(3000); 
    digitalWrite(elementPin,LOW); 
    delayMicroseconds(3000);      
  }

  Serial.print(element);
  Serial.print(" homed");
  
}
