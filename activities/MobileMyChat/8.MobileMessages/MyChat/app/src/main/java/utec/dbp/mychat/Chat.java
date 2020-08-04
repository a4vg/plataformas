package utec.dbp.mychat;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.widget.RecyclerView;
import android.support.v7.widget.LinearLayoutManager;
import android.widget.Toast;

import org.json.JSONArray;
import org.json.JSONException;

public class Chat extends AppCompatActivity {
    RecyclerView myView;
    RecyclerView.Adapter myAdapter;

    RequestsFlask rq = new RequestsFlask(this);



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_chat);

        myView = findViewById(R.id.main_recycler_view);
        myView.setLayoutManager(new LinearLayoutManager(this));

        rq.messages(new RequestsFlask.VolleyCallback() {
            @Override
            public void onSuccess(String resp) {
                JSONArray messages = null;
                try {
                    messages = new JSONArray(resp);
                    myAdapter = new MyAdapter(messages, Chat.this);
                    myView.setAdapter(myAdapter);


                } catch (JSONException e) {
                    e.printStackTrace();
                }
            }

            @Override
            public void onFailure(String error) {
                Toast.makeText(Chat.this, error, Toast.LENGTH_LONG).show();

            }
        });

    }
}
