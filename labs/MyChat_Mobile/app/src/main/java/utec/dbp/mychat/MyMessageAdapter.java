package utec.dbp.mychat;

import android.content.Context;
import android.support.annotation.NonNull;
import android.support.v7.widget.RecyclerView;
import android.util.Log;
import android.view.Gravity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.RelativeLayout;
import android.widget.TextView;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

public class MyMessageAdapter extends RecyclerView.Adapter<MyMessageAdapter.ViewHolder>  {
    public JSONArray elements;
    private Context mContext;
    private int userFromId;
    private static final String TAG = "MyMessageAdapter";

    public MyMessageAdapter(JSONArray elements, Context context, int userFromId) {
        this.elements = elements;
        this.mContext = context;
        this.userFromId = userFromId;
    }

    public class ViewHolder extends RecyclerView.ViewHolder {
        TextView friend_line;
        TextView my_line;
        RelativeLayout container;

        public ViewHolder(View itemView) {
            super(itemView);
            friend_line = itemView.findViewById(R.id.element_view_friend_line);
            my_line = itemView.findViewById(R.id.element_view_me_line);
            container = itemView.findViewById(R.id.element_view_container);
        }
    }

    @NonNull
    @Override
    public MyMessageAdapter.ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        Log.d(TAG, "onCreateViewHolder: ");
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.message_view, parent, false);
        return new MyMessageAdapter.ViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull MyMessageAdapter.ViewHolder holder, int position) {
        try {
            final JSONObject element = elements.getJSONObject(position);
            final String mFirstLine = element.getString("content");
            final int user_from_id = element.getInt("user_from_id");

            if(user_from_id == this.userFromId){
                holder.my_line.setText(mFirstLine);
                holder.friend_line.setText("");
            }else{
                holder.friend_line.setText(mFirstLine);
                holder.my_line.setText("");
            }

        } catch (JSONException e) {
            e.printStackTrace();
        }
    }

    @Override
    public int getItemCount() {
        return elements.length();
    }
}
