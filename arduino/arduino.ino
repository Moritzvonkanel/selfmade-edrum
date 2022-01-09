int sensors[10] = {A0, A1, A2, A3, A4, A5, A6, A7, A8, A9};

void setup() 
{
 Serial.begin(115200);
 Serial.setTimeout(1);
}

void loop() 
{
  //Ping to check usb devices for this e-drum arduino board
  if(Serial.available() && Serial.readString() == "SELFMADE_EDRUM_PING")
  {
    Serial.print("SELFMADE_EDRUM_PONG");
  }

  for (int i = 0; i < 10; i++) 
  {
    int value = analogRead(sensors[i]);

    if(value > 5) //Threshold
    {
      Serial.println("A"+ String(i) + ":" + String(value));
    }
  }
}
