package team.willcodeforfood.nsu.rescuer;

import android.annotation.SuppressLint;
import android.content.Context;
import android.content.Intent;

import androidx.appcompat.app.AppCompatActivity;

import android.net.Uri;
import android.os.Bundle;
import android.util.Log;
import android.view.MotionEvent;
import android.view.View;
import android.widget.ImageButton;

import com.google.android.exoplayer2.DefaultLoadControl;
import com.google.android.exoplayer2.DefaultRenderersFactory;
import com.google.android.exoplayer2.ExoPlayerFactory;
import com.google.android.exoplayer2.SimpleExoPlayer;
import com.google.android.exoplayer2.source.ExtractorMediaSource;
import com.google.android.exoplayer2.source.MediaSource;
import com.google.android.exoplayer2.trackselection.DefaultTrackSelector;
import com.google.android.exoplayer2.ui.PlayerView;
import com.google.android.exoplayer2.upstream.DefaultHttpDataSourceFactory;
import com.google.android.exoplayer2.util.Util;

import java.io.BufferedInputStream;
import java.io.DataInputStream;
import java.io.IOException;
import java.io.PrintStream;
import java.net.Socket;
import java.net.UnknownHostException;
import java.nio.charset.StandardCharsets;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class BotControlActivity extends AppCompatActivity
{

    // Tag to be used for debugging
    private static final String LOG_TAG = BotControlActivity.class.getSimpleName();
    private static final String STRING_KEY = "key";
    private static final String HTTP_REQUEST = "http://";
    private static final int CONTROL_PORT = 8080;
    private static final int STREAM_PORT = 8160;


    Socket rpiSocket = null;
    DataInputStream in = null;
    PrintStream out = null;


    PlayerView streamView;
    SimpleExoPlayer exoPlayer;

    String controlIP;
    String streamUri;

    boolean playWhenReady = true;
    long playbackPosition = 0;
    int currentWindow = 0;

    @SuppressLint("ClickableViewAccessibility")
    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_bot_control);

        streamView = findViewById(R.id.stream_view);

        controlIP = getIntent().getStringExtra(STRING_KEY);
        streamUri = HTTP_REQUEST + controlIP + ":" + STREAM_PORT;
        Log.v(LOG_TAG, "The Uri is: " + streamUri);

        ImageButton upButton = findViewById(R.id.up_button);
        ImageButton leftButton = findViewById(R.id.left_button);
        ImageButton rightButton = findViewById(R.id.right_button);
        ImageButton downButton = findViewById(R.id.down_button);
        ImageButton hardLeftButton = findViewById(R.id.hard_left_button);
        ImageButton hardRightButton = findViewById(R.id.hard_right_button);

        upButton.setOnTouchListener((v, event) ->
        {
            if (event.getAction() == MotionEvent.ACTION_DOWN)
            {
                BotControlActivity.this.senPai("W");
            } else if (event.getAction() == MotionEvent.ACTION_UP)
            {
                BotControlActivity.this.senPai("X");
            }
            return true;
        });

        leftButton.setOnTouchListener((v, event) ->
        {
            if (event.getAction() == MotionEvent.ACTION_DOWN)
            {
                BotControlActivity.this.senPai("A");
            } else if (event.getAction() == MotionEvent.ACTION_UP)
            {
                BotControlActivity.this.senPai("X");
            }
            return true;
        });

        rightButton.setOnTouchListener((v, event) ->
        {
            if (event.getAction() == MotionEvent.ACTION_DOWN)
            {
                BotControlActivity.this.senPai("D");
            } else if (event.getAction() == MotionEvent.ACTION_UP)
            {
                BotControlActivity.this.senPai("X");
            }
            return true;
        });

        downButton.setOnTouchListener((v, event) ->
        {
            if (event.getAction() == MotionEvent.ACTION_DOWN)
            {
                BotControlActivity.this.senPai("S");
            } else if (event.getAction() == MotionEvent.ACTION_UP)
            {
                BotControlActivity.this.senPai("X");
            }
            return true;
        });

        hardLeftButton.setOnTouchListener((v, event) ->
        {
            if (event.getAction() == MotionEvent.ACTION_DOWN)
            {
                BotControlActivity.this.senPai("L");
            } else if (event.getAction() == MotionEvent.ACTION_UP)
            {
                BotControlActivity.this.senPai("X");
            }
            return true;
        });

        hardRightButton.setOnTouchListener((v, event) ->
        {
            if (event.getAction() == MotionEvent.ACTION_DOWN)
            {
                BotControlActivity.this.senPai("R");
            } else if (event.getAction() == MotionEvent.ACTION_UP)
            {
                BotControlActivity.this.senPai("X");
            }
            return true;
        });
    }

    @Override
    public void onStart()
    {
        super.onStart();
        if (Util.SDK_INT > 23)
        {
            initializePlayer(streamUri);
        }
    }

    @Override
    public void onResume()
    {
        super.onResume();
        hideSystemUi();
        if ((Util.SDK_INT <= 23 || exoPlayer == null))
        {
            initializePlayer(streamUri);
        }
    }

    @Override
    public void onPause()
    {
        super.onPause();
        if (Util.SDK_INT <= 23)
        {
            releasePlayer();
        }
    }

    @Override
    public void onStop()
    {
        super.onStop();
        if (Util.SDK_INT > 23)
        {
            releasePlayer();
        }
    }

    private void initializePlayer(String src)
    {
        exoPlayer = ExoPlayerFactory.newSimpleInstance(
                new DefaultRenderersFactory(this),
                new DefaultTrackSelector(), new DefaultLoadControl());


        streamView.setPlayer(exoPlayer);
        streamView.setUseController(false);

        exoPlayer.setPlayWhenReady(playWhenReady);
        exoPlayer.seekTo(currentWindow, playbackPosition);

        Uri uri = Uri.parse(src);
        MediaSource mediaSource = buildMediaSource(uri);
        exoPlayer.prepare(mediaSource, true, false);
    }

    @org.jetbrains.annotations.NotNull
    private MediaSource buildMediaSource(Uri uri)
    {
        return new ExtractorMediaSource.Factory(
                new DefaultHttpDataSourceFactory("exoplayer")).
                createMediaSource(uri);
    }

    private void releasePlayer()
    {
        if (exoPlayer != null)
        {
            playbackPosition = exoPlayer.getCurrentPosition();
            currentWindow = exoPlayer.getCurrentWindowIndex();
            playWhenReady = exoPlayer.getPlayWhenReady();
            exoPlayer.release();
            exoPlayer = null;
        }
    }

    @SuppressLint("InlinedApi")
    private void hideSystemUi()
    {
        streamView.setSystemUiVisibility(View.SYSTEM_UI_FLAG_LOW_PROFILE
                | View.SYSTEM_UI_FLAG_FULLSCREEN
                | View.SYSTEM_UI_FLAG_LAYOUT_STABLE
                | View.SYSTEM_UI_FLAG_IMMERSIVE_STICKY
                | View.SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION
                | View.SYSTEM_UI_FLAG_HIDE_NAVIGATION);
    }

    public void senPai(String command)
    {
        ExecutorService executorService = Executors.newSingleThreadExecutor();

        executorService.execute(() ->
        {
            Log.v(LOG_TAG, "SenPai Called");
            try
            {
                rpiSocket = new Socket(controlIP, CONTROL_PORT);
                out = new PrintStream(rpiSocket.getOutputStream());
                in = new DataInputStream(new BufferedInputStream(rpiSocket.getInputStream()));

                out.println(command);

                byte[] bytes = new byte[1024];

                in.read(bytes);
                String reply = new String(bytes, StandardCharsets.UTF_8);
                Log.v(LOG_TAG, "Reply from server" + reply.trim());
                rpiSocket.close();
            } catch (UnknownHostException e)
            {
                Log.e(LOG_TAG, "Don't know about host: hostname");
            } catch (IOException e)
            {
                Log.e(LOG_TAG, "IOException:  " + e);
            }
        });
    }

    public static Intent buildIntent(Context context, String uri)
    {
        Intent intent = new Intent(context, BotControlActivity.class);
        intent.putExtra(STRING_KEY, uri);
        return intent;
    }
}
