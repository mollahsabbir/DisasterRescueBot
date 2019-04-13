package team.willcodeforfood.nsu.rescuer;

import android.net.Uri;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.MediaController;
import android.widget.Toast;
import android.widget.VideoView;

public class MainActivity extends AppCompatActivity {

    EditText addrField;
    Button btnConnect;
    VideoView streamView;
    MediaController mediaController;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        addrField = findViewById(R.id.addr);
        btnConnect = findViewById(R.id.connect);
        streamView = findViewById(R.id.streamview);

        btnConnect.setOnClickListener(new View.OnClickListener(){

            @Override
            public void onClick(View v) {
                String s = addrField.getEditableText().toString();
                playStream(s);
            }});
    }

    private void playStream(String src){
        Uri UriSrc = Uri.parse(src);
        if(UriSrc == null){
            Toast.makeText(MainActivity.this,
                    "UriSrc == null", Toast.LENGTH_LONG).show();
        }else{
            streamView.setVideoURI(UriSrc);
            mediaController = new MediaController(this);
            streamView.setMediaController(mediaController);
            streamView.start();

            Toast.makeText(MainActivity.this,
                    "Connect: " + src,
                    Toast.LENGTH_LONG).show();
        }
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        streamView.stopPlayback();
    }

}
