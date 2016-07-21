int PIEZOPIN = 5;

// One octave of notes between A4 and A5
int note_A3 = 220;
int note_A4 = 440;
int note_As4 = 466; int note_Bb4 = note_As4;
int note_B3 = 246.9;
int note_B4 = 494;
int note_C5 = 523.3;
int note_Cs5 = 554; int note_Db5 = note_Cs5;
int note_D5 = 587;
int note_Ds5 = 622; int note_Eb5 = note_Ds5;
int note_E5 = 659;
int note_F5 = 698;
int note_Fs5 = 740; int note_Gb5 = note_Fs5;
int note_G5 = 784;
int note_Gs5 = 830; int note_Ab5 = note_Gs5;
int note_C4=261.6;
int note_F4=349.2;
int note_E4=329.6;
int note_D4=293.7;


int note_G4=392;
int note_A5 = note_A4 * 2;
int note_As5 = note_As4 * 2; int note_Bb5 = note_As5;
int note_B5 = note_B4 * 2;

int note_rest = -1;

// note lengths defined here
long whole_note = 2000; // change tempo by changing duration of one measure
long half_note = whole_note / 2;
long quarter_note = whole_note / 4;
long eighth_note = whole_note / 8;
long sixteenth_note = whole_note / 16;

// WRITE YOUR SONG HERE

  
// if you want there to be silence between notes,
//   staccato should be true
bool staccato = true;

int piezo_pin=5;
void setup() {
  pinMode(PIEZOPIN, OUTPUT);
  
}

void loop() {
  tone(piezo_pin,note_C4,half_note );
  delay(half_note);
  tone(piezo_pin,note_C5 ,half_note);
  delay(half_note);
  tone(piezo_pin,note_B4 ,quarter_note);
  delay(quarter_note);
  tone(piezo_pin,note_G4 ,eighth_note );
  delay(eighth_note);
  tone(piezo_pin, note_A4, eighth_note);
  delay(eighth_note);
  tone(piezo_pin,note_B4,quarter_note );
  delay(quarter_note);
  tone(piezo_pin,note_C5,quarter_note );
  delay(quarter_note);
  delay(150);
  tone(piezo_pin,note_C4,half_note);
  delay(half_note);
  tone(piezo_pin,note_A4 ,half_note);
  delay(half_note); 
  tone(piezo_pin,note_G4 ,whole_note);
  delay(whole_note);
  delay(100);
  tone(piezo_pin,note_A3,half_note);
  delay(half_note);
  tone(piezo_pin,note_F4,half_note);
  delay(half_note);
  tone(piezo_pin,note_E4,quarter_note);
  delay(quarter_note);
  tone(piezo_pin,note_C4,eighth_note);
  delay(eighth_note);
  tone(piezo_pin,note_D4,eighth_note);
  delay(eighth_note);
  tone(piezo_pin,note_E4,quarter_note);
  delay(quarter_note);
  tone(piezo_pin,note_F4,quarter_note);
  delay(quarter_note);
  tone(piezo_pin,note_D4,quarter_note);
  delay(quarter_note);
  tone(piezo_pin,note_B3,eighth_note);
  delay(eighth_note);
  tone(piezo_pin,note_C4,eighth_note);
  delay(eighth_note);
  tone(piezo_pin,note_D4,quarter_note);
  delay(quarter_note);
  tone(piezo_pin,note_E4,quarter_note);
  delay(quarter_note);
  tone(piezo_pin,note_C4,half_note);
  delay(half_note);
  delay(2000);
      
  
  //PLAY YOUR SONG HERE
}
