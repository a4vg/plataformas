package utec.dbp.mychat;

import android.app.Activity;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.util.Log;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONException;
import org.json.JSONObject;

public class MessageActivity extends AppCompatActivity {
    public static final String EXTRA_USER_FROM_ID = "user_from_id";
    public static final String EXTRA_USER_TO_ID = "user_to_id";
    public static final String TAG = "MessageActivity";

    RecyclerView mRecyclerView;
    RecyclerView.Adapter mAdapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_message);
        mRecyclerView = findViewById(R.id.main_recycler_view);
        setTitle("jbell@...");
    }

    public Activity getActivity() {
        return this;
    }

    @Override
    protected void onResume() {
        super.onResume();

        mRecyclerView.setLayoutManager(new LinearLayoutManager(this));
        final String userFromId = getIntent().getExtras().get(EXTRA_USER_FROM_ID).toString();
        final String userToId = getIntent().getExtras().get(EXTRA_USER_TO_ID).toString();
        String url = "http://10.0.2.2:5000/chats/"+userFromId+"/"+userToId;
        RequestQueue queue = Volley.newRequestQueue(this);

        JsonObjectRequest jsonObjectRequest = new JsonObjectRequest(
                Request.Method.GET, url, null, new Response.Listener<JSONObject>() {
            @Override
            public void onResponse(JSONObject response) {
                try {
                    mAdapter = new MyMessageAdapter(response.getJSONArray("response"),getActivity(), Integer.parseInt(userFromId));
                    mRecyclerView.setAdapter(mAdapter);
                } catch (JSONException e) {
                    Log.d(TAG, e.getMessage());
                }
            }
        }, new Response.ErrorListener() {

            @Override
            public void onErrorResponse(VolleyError error) {
                Log.d(TAG, error.getMessage());
            }
        }
        );
        queue.add(jsonObjectRequest);
    }
}
