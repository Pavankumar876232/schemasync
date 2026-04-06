import { createClient } from "@supabase/supabase-js";

const supabase = createClient(
  "https://xxdgfjmnjdhcxkihyuzk.supabase.co",   // your project URL
  "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inh4ZGdmam1uamRoY3hraWh5dXprIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzU0NzA1MjksImV4cCI6MjA5MTA0NjUyOX0.XKCFXRRwRQaqiq6HC5KxlvGYt1ZxGhjqOaPUM3AdYD4"
);

export default supabase;