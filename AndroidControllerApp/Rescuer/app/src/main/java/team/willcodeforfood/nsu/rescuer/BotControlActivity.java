package team.willcodeforfood.nsu.rescuer;

import android.content.Context;
import android.content.Intent;
import android.net.Uri;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.MediaController;
import android.widget.VideoView;

public class BotControlActivity extends AppCompatActivity {

    VideoView streamView;
    MediaController mediaController;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_bot_control);

        streamView = findViewById(R.id.streamview);

    }

    public static Intent buildIntent(Context context, String uri){
        Intent intent = new Intent(context, BotControlActivity.class);
        intent.putExtra("key", uri);
        return intent;
    }
}
