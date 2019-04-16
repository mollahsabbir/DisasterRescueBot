package team.willcodeforfood.nsu.rescuer;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;

import com.google.android.material.button.MaterialButton;
import com.google.android.material.textfield.TextInputEditText;

import java.util.Objects;


public class MainActivity extends AppCompatActivity {

    // Tag to be used for debugging
    private static final String LOG_TAG =  MainActivity.class.getSimpleName();

    TextInputEditText addrField;
    MaterialButton connectButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        addrField = findViewById(R.id.addr_input);
        connectButton = findViewById(R.id.connect_button);

        // Start the searchProductActivity whenever the searchProduct toolbar is clicked
        connectButton.setOnClickListener(view ->
        {
            String uriString = Objects.requireNonNull(addrField.getText()).toString();
            Log.v(LOG_TAG, "The uri String is: " + uriString);

            startActivity(BotControlActivity.buildIntent(this, uriString));
        });
    }
}
